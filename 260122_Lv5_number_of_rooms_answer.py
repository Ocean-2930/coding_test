def solution(arrows):
    answer = 0
    
    # 방향 정의 (0부터 7까지 시계방향: 위, 오위, 오, 오아, 아, 왼아, 왼, 왼위)
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    
    now = (0, 0) # 현재 위치
    
    # 방문한 정점과 간선을 저장할 집합(Set)
    # 탐색 속도 O(1)을 위해 리스트가 아닌 Set 사용
    visited_nodes = set([now])
    visited_edges = set()
    
    for arrow in arrows:
        # 핵심 트릭: 대각선 교차(X자) 처리를 위해 1칸 이동을 2번으로 나누어 처리
        for _ in range(2):
            next_node = (now[0] + dx[arrow], now[1] + dy[arrow])
            
            # 방이 생성되는 조건:
            # 1. 이미 방문했던 점에 다시 도달했는가? (사이클 형성 가능성)
            # 2. 하지만 지금 타고 온 '이 길(간선)'은 처음인가? (되돌아온 게 아님)
            if next_node in visited_nodes:
                if (now, next_node) not in visited_edges:
                    answer += 1
            
            # 방문 기록 저장
            visited_nodes.add(next_node)
            
            # 간선은 양방향이므로 둘 다 저장 (A -> B, B -> A)
            visited_edges.add((now, next_node))
            visited_edges.add((next_node, now))
            
            # 위치 이동
            now = next_node
            
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
