from sys import argv, stdout
import re

episode_files = argv[:]


for episode in episode_files:
    title = ''
    exercise = False
    with open(episode, 'r') as infh:
        for line in infh.readlines():
            if line.strip().startswith('title: '):
                _, title = line.split(': ')
                stdout.write(f'## Episode: {title}')
            #elif line.strip().endswith(':::  challenge'):
            elif re.search(":::[:]*[ ]*challenge$", line.strip()):
                exercise = True
            else:
                #if line.strip().endswith(':::') or line.strip().endswith(':::  solution'):
                if re.search(":::$", line.strip()) or re.search(":::[:]*[ ]*solution$", line.strip()):
                    exercise = False
                elif exercise:
                    stdout.write(line)
