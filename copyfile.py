
def copy_file(source_file, destination_file): #both file names need to be str
    with open(source_file, 'rb') as s: 
        with open(destination_file, 'ab') as d: 
                chunk_size = 4096
                while True: 
                    chunk = s.read(chunk_size)
                    if not chunk: 
                        break 
                    d.write(chunk)

copy_file('testfile.mp4', 'test2.mp4')

