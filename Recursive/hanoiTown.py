# The Tower of Hanoi is a mathematical game or puzzle.
# This game is presented as follows:
#   There are 3 rods A, B, C. 
#   Rod A: a stack of n disks decreasing in diameter from bottom to top. 
#   Need to move this stack of disk from rod A to rod C according to the rule: 
#       Only 1 disc is transferred at a time. 
#       And only smaller diameter discs should be placed on top of larger diameter discs. 
#       During the transfer process, it is allowed to use rod B as an intermediate mean.
# The problem is: Finding a way that requires the least amount of disk movement
# -----------------------------------------------------------------------------------------

i = 0

def move(n, start, finish, spare):
    global i
    if n == 1:
        print("Move disk from %c to %c" % (start,finish))
        i += 1
        return
    else:
        move(n-1, start, spare, finish)
        move(1, start, finish, spare)
        move(n-1, spare, finish, start)

def main():
    disk = int(input("Please input number of disk: "))
    move(disk, '1', '3', '2')
    print("Total number of moves = %d\n" % i)
    return

if __name__ == '__main__':
    main()