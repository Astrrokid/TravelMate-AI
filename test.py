from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_graph

# res = tavily_search("Best travel destinations in Europe")
# print(res)

# res = search_flights("plan a 7 days japan trip from Lagos, Nigeria")
# print(res)
user_input = input("Enter your travel request: ")
response = run_travel_graph(user_input=user_input, thread_id="test_user")

print(response["answer"])