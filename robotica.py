quantidade_alunos, quantidade_amizades = [int(n) for n in input().split(" ")]

alunos_sem_grupo = list(range(1, quantidade_alunos + 1))
amigos = {}
for aluno in alunos_sem_grupo:
    amigos[aluno] = []

for i in range(quantidade_amizades):
    aluno1, aluno2 = [int(n) for n in input().split(" ")]

    amigos[aluno1].append(aluno2)
    amigos[aluno2].append(aluno1)

quantidade_grupos = 0
while len(alunos_sem_grupo) > 0:
    quantidade_grupos += 1

    grupo = [alunos_sem_grupo.pop(0)]
    while len(grupo) > 0:
        for i in range(len(grupo)):
            aluno = grupo.pop(0)

            for amigo in amigos[aluno]:
                if amigo not in alunos_sem_grupo:
                    continue

                grupo.append(amigo)
                alunos_sem_grupo.remove(amigo)

print(quantidade_grupos)