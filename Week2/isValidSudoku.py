def isValidSudoku(board):
    # initializing the hashmaps we need s
        d_row ={} ; d_col = {} ;  dict_of_numbers = {}

        dict_of_numbers = {i:0 for i in range(1,10)}
        #initialize our dictionaries
        for i in range(len(board)):
            d_row = {f'row{i}': dict_of_numbers for i in range(len(board))}
            d_col = {f'col{i}': dict_of_numbers for i in range(len(board))}
            d_grid = {f'grid{i}': dict_of_numbers for i in range(len(board))}

        # traversing through the board 
        for i in range(2,len(board)-1,3):
            for j in range(len(board[0])-1):
                if type(board[i][j]) != int:
                    continue
                d_row[f'row{i}'][board[i][j]] +=1 
                temp = d_row[f'row{i}'][board[i][j]]

                d_col[f'col{j}'][board[i][j]] +=1 
                temp2 =  d_col[f'col{j}'][board[i][j]]
                
                if temp > 1 or temp2 > 1 :
                    return False
                 

        return True



b = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]






print(len(b))