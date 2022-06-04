
# Returns -1 if nothing is installed.
def get_installed_revision(dir):
    try: 
        file = open(dir / '.tvn' / 'revision', "r")
        return int(file.read())
    except (FileNotFoundError, ValueError):
        try:
            # fallback to the original behavior
            file = open(dir / '.revision', "r")
            return int(file.read())
        except (FileNotFoundError, ValueError):
            pass
    
    return -1

def get_remote(dir):
    try:
        file = open(dir / '.tvn' / 'remote')
        return file.read()
    except (FileNotFoundError, ValueError):
        return "https://toast.openfortress.fun/toast/"
