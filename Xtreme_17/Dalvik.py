def calculate_R(A, B, C):
    v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18 = A, B, C, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

   
    #global v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12
    #v0, v1, v2, v3 = A, B, C, 1
    v4 = v3 - v3
    v5 = v4 - v3
    v6 = v3
    v7 = v4
    v7 = v7 - v1
    v8 = v0
    v9 = v0
    v9 = v0 + v1
    v10 = v4
    v11 = v4
    v12 = v3
    
    def l0():
        #global v11, v10, v13, v14, v15, v0, v1, v4
        v11 = v11 + v1
        v10 = v10 + v0
        v13 = v10
        v14 = v4
        v15 = v4 
        def l1():
            #global v16, v13, v1, v14, v15, v3
            v16 = v13 + v13
            if v16 <= v1:
                l2()
            
            v13 = v13 - v1
            v14 = v14 + v3
            v15 = v15 + v1
            l1()
            def l2():
                #global v13, v4
                if v13 > v4:
                    l3()
                v13 = v4 - v13  
                def l3():
                    #global v17, v18, v4, v3
                    v17 = v4
                    v18 = v3
                    def l4():
                        #global v17, v18, v13, v3, v6
                        v17 = v17 + v13
                        v18 = v18 + v3
                        if v18 <= v6:
                            l4()
                        v18 = v3   
                        def l5():
                            #global v17, v18, v13, v9, v4, v3, v12, v5, v6, v7, v8, v14, v15, v10
                            v17=v17-v9
                            v18=v18+v3
                            if v18<=v12:
                                l5()
                            if v17>=v4:
                                l6()
                            
                            v5 = v14
                            v6 = v12
                            v7 = v15
                            v8 = v10
                            v9 = v13
                            def l6():
                                #global v12, v3, v2
                                v12 = v12 + v3
                                if v12 <= v2:
                                    l0()
                    
    return v6

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    A, B, C = map(int, input().split())
    R = calculate_R(A, B, C)
    print(R)
