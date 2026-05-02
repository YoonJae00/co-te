def solution(players, callings):
    answer = []
    for i in range(len(callings)):
        call_name = callings[i] # 호명된 선수 이름 빼오기

        current_index = players.index(call_name) # 선수 위치 찾기


        # 위치 변경
        front_index = current_index - 1 
        temp = players[front_index]
        players[front_index] = players[current_index]
        players[current_index] = temp

    return answer