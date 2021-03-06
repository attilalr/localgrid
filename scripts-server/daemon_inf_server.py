import zerorpc, os, time, multiprocessing

port=4242

class glserver:
  def __init__(self,nodesfile):
    self.nodesfile=nodesfile

  def chk_conn(self):
    return 'connected'

  def chk_load(self, name):
    try:
      file=open(self.nodesfile,'r')
    except:
      return "error opening file."

    linha=file.readline()
    while(linha):
      if name.lower() in linha.split():
        return linha.split()[2]
      linha=file.readline()
    return "Error - hostname not found."

  def chk_stats(self, name):
    try:
      file=open(self.nodesfile,'r')
    except:
      return "error opening file."
    linha=file.readline()
    while(linha):
      if name.lower() in linha.split():
        return linha.split()[1]
        print linha.split()[1]
      linha=file.readline()
    return "Error - hostname not found."

def start_server(nodesfile):
  s = zerorpc.Server(glserver(nodesfile))
  s.bind("tcp://0.0.0.0:"+str(port))
  s.run()

def eternal_loop(nodesfile):
  # sleep for a interval and gather information after that
  #for i in range(100):
  while(1):
    print "main loop "
    update_nodes_stats(nodesfile)
    time.sleep(100)

def update_nodes_stats(nodesfile):
  # scan the /etc/hosts
  hosts=os.popen("cat /etc/hosts|grep .gridlan|awk {'print $3'}").read().split()

  string=''

  for hostname in hosts:
    # checar se esta on
    if 'ttl=64' in os.popen('ping -c1 '+hostname.lower()).read():
      status='on'
    else:
      status='off'
    # checar quantos processos
    if status=='on':
      njobs=os.popen('rsh '+hostname.lower()+' ps axr|grep -v "ps axr"|wc -l').read()[:-1]
    else:
      njobs=0
    # write
    string=string+hostname.lower()+' '+status+' '+str(njobs)+'\n'

  print string
      
  try: 
    file=open(nodesfile,'w')
    file.write(string)
    file.close()
  except:
    print "error opening nodesfile for writing."
      


###### MAIN #####################################

nodesfile='/opt/gridlan/nodes.status'

jobs=list()
#start main loop
p = multiprocessing.Process(target=eternal_loop,args=(nodesfile,))
jobs.append(p)
p.start()
#start rpc server
p = multiprocessing.Process(target=start_server, args=(nodesfile,))
jobs.append(p)
p.start()

