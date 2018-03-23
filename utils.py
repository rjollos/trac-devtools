import subprocess


trac_url = 'https://rjollos:%s@trac-hacks.org/login/rpc'


def get_lp_password():
    proc = subprocess.Popen(['lpass', 'show', '--sync', 'no', '--password',
                             'Edgewall/trac-hacks.org'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    proc.stdout.close()
    proc.stderr.close()
    if proc.returncode == 0:
        return stdout.strip()
    else:
        print('ERROR: ', stderr)
