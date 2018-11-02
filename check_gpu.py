import subprocess

p = subprocess.Popen(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
nvidia_smi = [line.strip() for line in p.stdout.readlines()]

start_i = 36
process_lines = [line.split()[2] for line in nvidia_smi[start_i:-1]]
docker_ids = [''] * len(process_lines)
docker_names = [''] * len(process_lines)

#pid -> container id
for i,pid in enumerate(process_lines):
	p2 = subprocess.Popen(['cat', '/proc/{}/cgroup'.format(pid)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	docker_ids[i] = p2.stdout.readlines()[0].split(':')[-1][8:20]

#container id -> container names
p3 = subprocess.Popen(['docker', 'ps'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
docker_ps = [line.strip().split() for line in p3.stdout.readlines()]
for i,docker_id in enumerate(docker_ids):
	for container in docker_ps:
		if container[0] == docker_id:
			docker_names[i] = container[-1]
			break

#display
for i,line in enumerate(nvidia_smi):
	if start_i <= i < start_i+len(process_lines):
		print(line + ' -> ' + docker_names[i-start_i])
	else:
		print(line)


