import time
import random


class Point:
    
    def __init__(self,value,column,row):
        self.row = row #the row the point is in
        self.column = column #the column the point is in
        self.value = value # the value of the point
        
        #the following defines the subgrid the point is in
        if self.row <=3 and self.column<=3:
            self.subgrid = 1
        
        if self.row <=3 and self.column<=6 and self.column > 3:
            self.subgrid = 2

        if self.row <=3 and self.column > 6:
            self.subgrid = 3
            
        if self.row <=6 and self.row >3 and self.column<=3:
            self.subgrid = 4
            
        if self.row <=6 and self.row > 3 and self.column<=6 and self.column >3:
            self.subgrid = 5
            
        if self.row <=6 and self.row > 3 and self.column > 6:
            self.subgrid = 6
            
        if self.row > 6 and self.column <=3:
            self.subgrid = 7
            
        if self.row > 6 and self.column <=6 and self.column >3:
            self.subgrid = 8
            
        if self.row > 6 and self.column > 6:
            self.subgrid = 9
        
        #a list of all the important attributes of the point
        self.list = [self.value,self.column,self.row,self.subgrid]
        
    def __repr__(self):
        return str(self.list)
    
    
    
        
def point_test(point,grid):
    """
    Checks a point in a given grid to see if it is allowed or not
    Returns True is allowed, False if not 
    Given point should always have non-zero value
    """
    if point.value == 0:
        return False
    
    for other in grid.grid_list:
        if other==point:
            continue
        if other.row == point.row or other.column == point.column or other.subgrid == point.subgrid:
            if other.value == point.value:
                return False
        
    return True
        
        
        
        
class Sudoku:
    
    grid_list = []
    def __init__(self):
        self.construct()
        self.values = [point.value for point in self.grid_list]
    
    #this constructs the 'grid' as a list of all the points on the grid
    def construct(self):
        for i in range(1,10):
            for j in range(1,10):
                self.grid_list.append(Point(0,j,i))
    #this prints a grid to the terminal            
    def show(self):
        print('COLUMN NUMBERS')
        print(' 1 2 3 4 5 6 7 8 9')
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 1'.format(*[self.grid_list[i].value for i in range(0,9)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 2'.format(*[self.grid_list[i].value for i in range(9,18)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 3'.format(*[self.grid_list[i].value for i in range(18,27)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 4'.format(*[self.grid_list[i].value for i in range(27,36)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 5'.format(*[self.grid_list[i].value for i in range(36,45)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 6'.format(*[self.grid_list[i].value for i in range(45,54)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 7'.format(*[self.grid_list[i].value for i in range(54,63)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}|ROW 8'.format(*[self.grid_list[i].value for i in range(63,72)]))
        print('___________________')
        print('|{}|{}|{}|{}|{}|{}|{}|{}|{}| ROW 9'.format(*[self.grid_list[i].value for i in range(72,81)]))
        print('___________________')
        
    #this allows a user to define points on the grid
    #it is quite long and tedious so might try improve but for now it works
    #integers will work, non-integers won't, inputting 'end' will end this
    def user_define(self):
        print('This will allow you to define the given values in your sudoku puzzle')
        print('It will ask for every point by its column and row number')
        print('Input the given value as a number or \'n\' for no value')
        for i in range(len(self.grid_list)):
            new_value = input('What value is given in the square at column '+str(self.grid_list[i].column)+' and row ' + str(self.grid_list[i].row)+'? (Input \'n\' for a blank): ')
            print('You input',new_value)
            if new_value == 'end':
                break
            try:
                new_value = int(new_value)
                self.grid_list[i].value = new_value
                print(self.grid_list[i].value)
            except Exception:
                pass
            grid.show()
    
    
    #this method will test the grid to see if it is good 
    def test(self):
        no_bad_points = 0
        good_list = [1,2,3,4,5,6,7,8,9]
        for point in self.grid_list:
            numbers_in_row = [point.value]
            numbers_in_column = [point.value]
            numbers_in_subgrid = [point.value]
            for other in self.grid_list:
                # do nothing if they are the same point
                if point == other:
                    pass
                
                #otherwise make a list of all the numbers in row,column and subgrid
                else:
                    if point.row == other.row:
                        numbers_in_row.append(other.value)
                        
                    if point.column == other.column:
                        numbers_in_column.append(other.value)       
                    
                    if point.subgrid == other.subgrid:
                        numbers_in_subgrid.append(other.value)
                        
            #sort the lists to make sure boolean check is fine            
            numbers_in_row.sort()
            numbers_in_column.sort()
            numbers_in_subgrid.sort()
            
            if numbers_in_column != good_list or numbers_in_row != good_list or numbers_in_subgrid != good_list: 
                no_bad_points += 1
            
    
        if no_bad_points == 0:
            return True
        
        else:
            return False
        
        
        
    #the method to solve the sudoko    
    def solve(self):
        print('We are solving:')
        self.show()
        print('Starting in 5 seconds')
        time.sleep(5)
        print('Solve method running')
        start = time.time()
        #generating list of indices of unknown values
        #so we don't change defined values
        #THIS BIT IS FINE
        indices_unknown = [] 
        for point in self.grid_list:
            if point.value == 0:
                indices_unknown.append(self.grid_list.index(point))
        x=0        
        while x < len(indices_unknown)-1:
            i = indices_unknown[x]
            point = self.grid_list[i]
            if point.value == 9:
                point.value = 0
                x -= 1
            else:
                point.value += 1
            print('Changing point {}/81'.format(i+1))
            #self.show()
            if point_test(point,self):
                x += 1
            
            else:
                if point.value == 9:
                    point.value = 0
                    x -= 1    

                    
                    
        self.show()
        end = time.time()
        time_taken = end - start
        print('Solved! It took {} seconds to solve'.format(time_taken))
                
                
            
        
                

        
if __name__=='__main__':
    grid = Sudoku() 
    grid.show()         
    grid.user_define()
    grid.solve()


#EASY sudoku
# =============================================================================
#    grid.grid_list[1].value = 7
#    grid.grid_list[4].value = 2
#    grid.grid_list[7].value = 4
#    grid.grid_list[8].value = 6
#    grid.grid_list[10].value = 6
#    grid.grid_list[15].value = 8
#    grid.grid_list[16].value = 9
#    grid.grid_list[18].value = 2
#    grid.grid_list[21].value = 8
#    grid.grid_list[24].value = 7
#    grid.grid_list[25].value = 1
#    grid.grid_list[26].value = 5
#    grid.grid_list[28].value = 8
#    grid.grid_list[29].value = 4
#    grid.grid_list[31].value = 9
#    grid.grid_list[32].value = 7
#    grid.grid_list[36].value = 7
#    grid.grid_list[37].value = 1
#    grid.grid_list[43].value = 5
#    grid.grid_list[44].value = 9
#    grid.grid_list[48].value = 1
#    grid.grid_list[49].value = 3
#    grid.grid_list[51].value = 4
#    grid.grid_list[52].value = 8
#    grid.grid_list[54].value = 6
#    grid.grid_list[55].value = 9
#    grid.grid_list[56].value = 7
#    grid.grid_list[59].value = 2
#    grid.grid_list[62].value = 8
#    grid.grid_list[64].value = 5
#    grid.grid_list[65].value = 8
#    grid.grid_list[70].value = 6
#    grid.grid_list[72].value = 4
#    grid.grid_list[73].value = 3
#    grid.grid_list[76].value = 8
#    grid.grid_list[79].value = 7
#    grid.show()
#    grid.solve()
# =============================================================================

    
#MEDIUM sudoku

##    grid.grid_list[1].value = 3
#    grid.grid_list[5].value = 9
#    grid.grid_list[8].value = 8
#    grid.grid_list[12].value = 2
#    grid.grid_list[15].value = 1
#    grid.grid_list[18].value = 4
#    grid.grid_list[20].value = 2
#    grid.grid_list[21].value = 8
#    grid.grid_list[25].value = 5
#    grid.grid_list[26].value = 3
#    grid.grid_list[27].value = 6
#    grid.grid_list[33].value = 2
#    grid.grid_list[36].value = 1
#    grid.grid_list[38].value = 7
#    grid.grid_list[41].value = 2
#    grid.grid_list[44].value = 5
#    grid.grid_list[47].value = 5
#    grid.grid_list[49].value = 1
#    grid.grid_list[53].value = 4
#    grid.grid_list[61].value = 8
#    grid.grid_list[66].value = 3
#    grid.grid_list[78].value = 9
#    grid.grid_list[79].value = 4
#    grid.grid_list[80].value = 1
#  
#    
#    
#    grid.show()
#    grid.solve()
#    grid.solve()