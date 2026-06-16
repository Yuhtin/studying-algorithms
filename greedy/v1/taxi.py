from collections import Counter

n = int(input())
cnt = Counter(map(int, input().split()))

ans = cnt[4]

ans += cnt[3]
cnt[1] = max(0, cnt[1] - cnt[3])

ans += cnt[2] // 2

if cnt[2] % 2:
    ans += 1
    cnt[1] = max(0, cnt[1] - 2)
    
ans += (cnt[1] + 3) // 4

print(ans)