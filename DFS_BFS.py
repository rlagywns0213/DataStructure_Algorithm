from collections import deque #for bfs

class search_graph:
    def __init__(self):
        #인접노드위함 - 8개의 노드를 처리할 수 있는 원소 9개
        self.graph = [
            [],
            [2,3,8],
            [1,7],
            [1,4,5],
            [3,5],
            [3,4],
            [7],
            [2,6,8],
            [1,7]           
        ]
        #방문 정보 표현
        self.visited = [False] * 9 

    def dfs(self, v):
        # 현재 노드 방문 처리
        self.visited[v] = True
        print(v, end = ' ')
        # 현재 노드와 연결된 다른 노드 재귀적 방문
        for i in self.graph[v]:
            if not self.visited[i]:
                self.dfs(i)


    def bfs(self, start):
        # 큐 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        # 현재 노드 방문 처리
        self.visited[start] = True
        # 큐가 empty일 때까지
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력하기
            v = queue.popleft()
            print(v, end= ' ')
            # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            for i in self.graph[v]:
                if not self.visited[i]:
                    queue.append(i)
                    self.visited[i] = True

sg = search_graph()
print("\n depth first search")
sg.dfs(1)
print("\n breadth first search") 
sg.visited = [False] * 9
sg.bfs(1)