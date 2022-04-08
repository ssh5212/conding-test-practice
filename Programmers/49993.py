def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        now_tree = 0
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] not in skill:
                continue
            elif skill[now_tree] == skill_trees[i][j]:
                now_tree += 1
            else:
                now_tree = -1
                break
        if now_tree != -1:
            answer += 1
    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))