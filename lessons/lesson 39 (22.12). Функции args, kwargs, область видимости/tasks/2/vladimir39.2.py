def prepare_request(**endpoint):
    if not endpoint:
       raise ValueError("Нужно передать хотя бы один балл")
    timeout=endpoint.get(5)
    retries=endpoint.get(3)
    payload={"None","static"}
    extras={key: value for key, value in endpoint.items() if key in payload}
    return  {
             "endpoint": endpoint,
             "control": {"timeout": timeout, "retries": retries},
             "payload": {"data": [1, 2]}
           } 

print(prepare_request(endpoint="/stats", data=[1, 2]))
print(prepare_request(endpoint="/sync", timeout=10, retries=0, mode="fast"))
