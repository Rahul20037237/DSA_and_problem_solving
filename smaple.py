def method(tickets,tickets_count):
    tickets.sort()
    result=[1]*tickets_count
    for i in range(tickets_count):
        for j in range(i):
            if abs(tickets[i] - tickets[j]) <= 1:
                result[i]=max(result[i],result[j]+1)
    return max(result)

print(method([8,4,4,5,8],5))