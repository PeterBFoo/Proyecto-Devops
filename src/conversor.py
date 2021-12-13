import os

n_archivo = 1


def conversor(output):

    assert isinstance(output, list)

    global n_archivo
    ext_archivo = '.md'
    file = open(
        os.path.join(os.getcwd(), str(n_archivo) + ext_archivo), "w")

    for element in output:
        file.write(str(element) + os.linesep)
    file.close()

    print('¡Archivo ' + str(n_archivo) + ' convertido correctamente!')
    n_archivo += 1

    return