import subprocess




def reload_tor():
    try:
        subprocess.run("sudo systemctl restart tor")
    except:
        pass