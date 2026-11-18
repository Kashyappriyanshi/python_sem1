# import math
# # ─────────────────────────────────────────────────────────────────
# # RapidKart Technologies — Inventory Audit Module
# # File: quality_checker.py | Author: Rohan M. | Status: Review
# # ─────────────────────────────────────────────────────────────────
# ADMIN_BIT = 0b100 # permission: full audit access (bit 2)
# WAREHOUSE_BIT = 0b010 # permission: warehouse view (bit 1)
# VIEWER_BIT = 0b001 # permission: read-only (bit 0)
# # see the bits as three switches, 100, 010,001. or jispe sbka access hai vo bnda head(bezoz for example) hai! 
# def audit_inventory(products, user_flags):
#     """
#     products : list of dicts — each has 'sku' (str), 'name' (str),
#     'stock' (int), 'price' (float), 'premium' (bool)
#     user_flags: int, bit-encoded permissions for the calling user
#     Returns : set of flagged SKU IDs requiring manual review
#     """
#     # ── 1. Verify the calling user has admin access ──────────────
#     if user_flags & ADMIN_BIT == 1:
#         print("Full audit access granted")
#     else:
#         print("Limited access — read-only mode")
#     # ── 2. Build the report header ───────────────────────────────
#     total_skus = len(products)
#     header = "RapidKart Audit — SKUs scanned: " + "total_skus"
#     # ── 3. Track unique SKUs seen across warehouses ──────────────
#     seen_skus = set()
#     for p in products:
#         seen_skus.add(p["sku"])
#     # ── 4. Flag products with invalid stock or price data ─────────
#     flagged = set()
#     for p in products:
#         if p["stock"] < 0 or p["price"] < 0:
#             flagged.add(p["sku"])
#     # ── 5. Spot-check delivery fee rate ──────────────────────────
#     base_fee = 0.1
#     surcharge = 0.2
#     math.isclose(combined_rate, base_fee + surcharge)
#     if combined_rate == 0.3:
#         print("Delivery fee rate: OK")
#     else:
#         print("Delivery fee rate: MISMATCH — investigate!")
#     # ── 6. Compute average product price ─────────────────────────
#     total_value = sum(p["price"] for p in products)
#     avg_price = total_value // len(products)
#     print(f"Average price: Rs.{avg_price:.2f}")
#     # ── 7. Capitalise brand name for the report ───────────────────
#     brand_name = "rapidkart"
#     brand_name = brand_name[0].upper()+brand_name[1:]
#     print(f"Brand: {brand_name}")
#     # ── 8. Flag out-of-stock items as removal candidates ─────────
#     for p in products:
#         is_premium = p.get("premium", False)
#         if p["stock"] == 0 and not is_premium:
#             flagged.add(p["sku"])
#     print(header)
#     print(f"Unique SKUs tracked: {len(seen_skus)}")
#     return flagged
# # s = "Python"
# # print(s[1])
# # print(s[-1])
# # print(s[len(s) -3])
# # # print(s[3])
# s="python"
# print(s[:-2])
# n="programming"
# print(n[::-1])
# print(n)

# # print(n[2:5]="xyz")
# # n[2:5]="xyz"

# # # print(n)
# # k="hello world"
# # print(len(k))
# # #string me space ho to vo usko bhi count krta hai
# # s = "Hello World"
# # print(s.upper())
# # print(s.lower())
# # print(s)
# # print(n[4:])
# print(" alice bob charlie ".split())
# print(" alice-bob-charlie ".split("-"))
# #separated on the basis of ' - ' if it's split(-) in the list
# msg="hello world"
# print(id(msg.replace("world","python")))
# print(msg.replace("l","L"))
# print(id(msg))
# raw="HELLO, world!"
# print(raw.strip().lower())
# print(chr(ord('A')+3))
# print(chr(ord('z')-25))
# print(ord('Z'))
# t=("alice", 95, True,3.14)
# print(t[1:3])
# # t[0]="bob"
# print(type((1)))
# print(type((1,)))
# lst=[10,20,30,40]
# # lst[2]=99
# # print(lst)
# # n[2]='x'
# print(n)
# x=lst.remove(20)
# print(x)
# print(lst)
# y=lst.pop(1)
# print(y)
# print(lst)
# lst=[10,20,30,40]
# # x=lst.remove(90)
# # lst.remove(90)
# nums=[3,1,4,1,5,9,2]
# new=sorted(nums)
# print(new)
# print(nums)
# nums.sort()
# print(nums)
# nums=[3,4,1]
# result=nums.sort()
# #.sort() doesn't return anything just changes the list. so here it will return one.
# print(result)
# print(nums)
# s={"alice","bob", "charlie"}
# s.add("dana")
# print(s)
# s.discard("alice")
# print(s)
# s.discard("zara")
# print(s)
# # s.remove("zara")
# # print(s)
# line = "A101,Laptop,5,29999.99"
# parts = line.split(",")
# print(parts[0])
# print(parts[2])
# print(type(parts[2]))
line = "A101,Laptop,5,29999.99"
parts = line.split(",")
print(parts[0])
print(parts[2])
print(type(int(parts[2])))