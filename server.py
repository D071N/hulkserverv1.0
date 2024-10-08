from flask import Flask, render_template
import subprocess
import os 
import signal

app = Flask(__name__)

bot_process = subprocess.Popen(['python3' , 'run.py'])


def kill_subprocesses():
    current_pid = os.getpid()
    cmd = f'pgrep -P {current_pid}'
    pids = subprocess.check_output(cmd, shell=True).decode().split()
    for pid in pids:
        try:
            os.kill(int(pid), signal.SIGTERM)
        except OSError:
            pass




@app.route("/")
def page_web_de_mort():
    bot_process
    return "<html><body><img src='https://c.tenor.com/e2VK6sB1TX0AAAAd/tenor.gif'></body></html>"
    #page_web_de_mort()
    
@app.route("/kill")
def killswitch():
    kill_subprocesses()
    p = subprocess.Popen(f'refresh', stdout=subprocess.PIPE, shell=True)
    output, error = p.communicate()
    bot_process
    return "<html><body><img src='https://c.tenor.com/e2VK6sB1TX0AAAAd/tenor.gif'></body></html>"
    #page_web_de_mort()    
    

app.run()
