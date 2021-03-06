import zerorpc, os, time, datetime

connection='tcp://server_ip:4242'
vbox_interface='VirtualBox Host-Only Ethernet Adapter #3'

def restart(prog_files_path):
  os.system('taskkill /F /IM vboxheadless.exe')
  os.system('net stop openvpnservice')
  os.system('netsh interface set interface name="Gridlan Bridge" admin=disable')
  os.system('netsh interface set interface name="Gridlan Bridge" admin=enable')
  os.system('net start openvpnservice')
  os.system('cd "'+prog_files_path+'\\oracle\\virtualbox" && vboxmanage dhcpserver remove --ifname "'+vbox_interface+'" & vboxmanage startvm node --type headless')

##### MAIN #####################################

RESTART=1 # Option to make the script restart the system, 0 is for log test purpose

if 'PROGRAMW6432' in os.environ:
  program_files_path=os.environ['PROGRAMW6432']
else:
  program_files_path=os.environ['programfiles']

if (RESTART==1):
  print "Restarting the gridlan client..."
  restart(program_files_path)
  print "Ok."
  time.sleep(8)
  sys.exit(0)

def log(msg):
  try:
    file=open(program_files_path+'\\gridlan\heartbeat.log','a')
    file.write(str(datetime.datetime.today())+": "+msg+'\n')
    file.close()
  except:
    print "Problem opening log file."
    print "Trying to acess "+os.environ['programfiles']+'\\gridlan\heartbeat.log'

try:
  hostname=os.popen('more "'+program_files_path+'\\gridlan\\hostname.txt"').read().split()[0]
  print "hostname: "+hostname
except:
  print "Problem getting hostname."

c = zerorpc.Client()

try:
  c.connect(connection)
  log("connected")
  if c.chk_stats(hostname)=='off':
    log("running restart script!")
    restart(program_files_path)
  else:
    log(c.chk_stats(hostname))
except:
  pass

