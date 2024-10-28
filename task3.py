import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)

    def is_empty(self):
        return not bool(self.queue)

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = PriorityQueue()
    priority_queue.enqueue(start, 0)

    while not priority_queue.is_empty():
        distance, current_vertex = priority_queue.dequeue()

        # Якщо поточна відстань більша за збережену - немає сенсу продовжувати
        if distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.enqueue(neighbor, distance)

    return distances

# Приклад графа у вигляді словника з конспекту
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

print(dijkstra(graph, 'A'))
