import networkx as nx
import matplotlib.pyplot as plt

# 도로 네트워크 그래프 생성
G = nx.DiGraph()

# 교차로 및 도로 추가
G.add_edge("출발지", "목적지1", weight=5)  # 출발지에서 목적지1로 가는 도로
G.add_edge("목적지1", "목적지2", weight=7)  # 목적지1에서 목적지2로 가는 도로
G.add_edge("목적지2", "도착지", weight=3)  # 목적지2에서 도착지로 가는 도로

# 도로 상황 고려
traffic_conditions = {
    ("목적지1", "목적지2"): 0.2,  # 목적지1에서 목적지2로 가는 도로의 혼잡도
    ("목적지2", "도착지"): 0.3,  # 목적지2에서 도착지로 가는 도로의 혼잡도
}

# 경로 계획 함수
def plan_optimal_route(G, start, end, traffic_conditions):
    # 가중치를 혼잡도에 따라 업데이트
    for u, v in G.edges():
        if (u, v) in traffic_conditions:
            G[u][v]['weight'] *= (1 - traffic_conditions[(u, v)])

    # 최적 경로 계산
    optimal_path = nx.shortest_path(G, source=start, target=end, weight='weight', method='dijkstra')

    return optimal_path

# 출발지와 목적지 설정
start_location = "출발지"
end_location = "도착지"

# 최적 경로 계산
optimal_route = plan_optimal_route(G, start_location, end_location, traffic_conditions)

# 결과 출력
print("최적 경로:", optimal_route)

# 도로 네트워크 시각화
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
