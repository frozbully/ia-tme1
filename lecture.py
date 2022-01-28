def fileEtu (filepath) :
    """retourne une matrice des preferences a partir d'un fichier"""
    f = open(filepath, 'r')
    content = f.readlines()
    f.close()
    #nbetu = content[0]
    preferences = [line.split()[1:] for line in content[1:]]
    return preferences

def fileSpe (filepath) :
    """retourne une matrice des preferences a partir d'un fichier"""
    f = open(filepath, 'r')
    content = f.readlines()
    f.close()
    #nbetu = content[0].split()[1]
    cap = content[1].split()[1:]
    preferences = [line.split()[1:]+[cap[int(line.split()[0])]] for line in content[2:]]
    return preferences