class Solution:
    def solve(self, board) -> None:
        if len(board)==0:
            return
        lb = 0
        rb = len(board[0][:])-1
        ub = 0
        db = len(board)-1
        if(rb==0 and db==0):
            return 
        l=(0,-1)
        r=(0,1)
        u=(-1,0)
        d=(1,0)
        queue = []
        result = []
        his=set()
        # print(board[-1])
        for i in range(rb):
            if board[0][i]=='O':
                queue.append((0,i))
        #左上角去重复
        for i in range(1,db):
            if board[i][0]=='O':
                queue.append((i,0))
        for i in range(db):
            if board[i][rb]=='O':
                queue.append((i,rb))
        #右下角db+1
        for i in range(rb+1):
            if board[db][i]=='O':
                queue.append((db,i))
        print(queue)
        result = set(queue)
        while queue:
            next_queue = []
            for k in queue:
                #to left
                his.add(k)
                if k[1]+l[1]>=lb and board[k[0]][k[1]+l[1]]=='O' and (k[0],k[1]+l[1]) not in his:
                    next_queue.append((k[0],k[1]+l[1]))
                    result.add((k[0],k[1]+l[1]))
                #to right
                if k[1]+r[1]<=rb and board[k[0]][k[1]+r[1]]=='O' and (k[0],k[1]+r[1]) not in his:
                    next_queue.append((k[0],k[1]+r[1]))
                    result.add((k[0],k[1]+r[1]))
                #to up
                if k[0]+u[0]>=ub and board[k[0]+u[0]][k[1]]=='O' and (k[0]+u[0],k[1]) not in his:
                    next_queue.append((k[0]+u[0],k[1]))
                    result.add((k[0]+u[0],k[1]))
                #to down
                if k[0]+d[0]<=db and board[k[0]+d[0]][k[1]]=='O' and (k[0]+d[0],k[1]) not in his:
                    next_queue.append((k[0]+d[0],k[1]))
                    result.add((k[0]+d[0],k[1]))
            queue=next_queue

        print(result)
        queue_m_board=[(0,0)]
        his_m_board=set()
        while queue_m_board:
            next_queue = []
            for k in queue_m_board:
                if board[k[0]][k[1]]=='O' and (k[0],k[1]) not in result:
                    board[k[0]][k[1]]='X'
                #to left
                if k[1]+l[1]>=lb and (k[0],k[1]+l[1]) not in his_m_board:
                    next_queue.append((k[0],k[1]+l[1]))
                    his_m_board.add((k[0],k[1]+l[1]))
                #to right
                if k[1]+r[1]<=rb and (k[0],k[1]+r[1]) not in his_m_board:
                    next_queue.append((k[0],k[1]+r[1]))
                    his_m_board.add((k[0],k[1]+r[1]))
                #to up
                if k[0]+u[0]>=ub and (k[0]+u[0],k[1]) not in his_m_board:
                    next_queue.append((k[0]+u[0],k[1]))
                    his_m_board.add((k[0]+u[0],k[1]))
                #to down
                if k[0]+d[0]<=db and (k[0]+d[0],k[1]) not in his_m_board:
                    next_queue.append((k[0]+d[0],k[1]))
                    his_m_board.add((k[0]+d[0],k[1]))
            queue_m_board=next_queue
        return

        



if __name__ == "__main__":
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # board = [["X","O","X","O","X","O"],
    #          ["O","X","O","X","O","X"],
    #          ["X","O","X","O","X","O"],
    #          ["O","X","O","X","O","X"]]
    board =[["X","O","O","X","X","X","O","X","X","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","X","X","O","O","X","O","O","O","X","O","X","O","X","O","O","X","O"],["O","O","O","X","X","X","X","O","X","O","X","X","O","O","O","O","X","O","X","O"],["O","O","O","X","X","O","O","X","O","O","O","X","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","X","X","X","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","X","O","X","X","O","O","O","O","O","O","X","O","X"],["O","O","O","X","O","O","O","X","O","X","O","X","O","X","O","X","O","X","O","X"],["O","O","O","X","O","X","O","O","X","X","O","X","O","X","X","O","X","X","X","O"],["O","O","O","O","X","O","O","X","X","O","O","O","O","X","O","O","O","X","O","X"],["O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O","X","O"],["X","O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O"],["O","X","O","O","O","X","O","X","O","X","X","O","X","X","X","O","X","X","O","O"],["X","X","O","X","O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","X"],["O","X","O","O","X","X","X","O","O","O","X","X","X","X","X","O","X","O","O","O"],["O","O","X","X","X","O","O","O","X","X","O","O","O","X","O","X","O","O","O","O"],["X","O","O","X","O","X","O","O","O","O","X","O","O","O","X","O","X","O","X","X"],["X","O","X","O","O","O","O","O","O","X","O","O","O","X","O","X","O","O","O","O"],["O","X","X","O","O","O","X","X","X","O","X","O","X","O","X","X","X","X","O","O"],["O","X","O","O","O","O","X","X","O","O","X","O","X","O","O","X","O","O","X","X"],["O","O","O","O","O","O","X","X","X","X","O","X","O","O","O","X","X","O","O","O"]]
    print(board)
    Solution().solve(board)
    print(board)