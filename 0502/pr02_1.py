def solution(players, callings):
    # 딕셔너리 사용 index 사용시 처음부터 훑어서 시간이 매우 오래걸림
    player_dict = {name: i for i, name in enumerate(players)}
    
    for call in callings:
        curr_idx = player_dict[call]
        prev_idx = curr_idx - 1
        
        prev_player = players[prev_idx]
        
        players[prev_idx], players[curr_idx] = players[curr_idx], players[prev_idx]
        
        player_dict[call] = prev_idx
        player_dict[prev_player] = curr_idx
        
    return players