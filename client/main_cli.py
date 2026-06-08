from cli.front import UserFrontendCLI
import sys
token = sys.argv[1]
if __name__ == '__main__':
    front = UserFrontendCLI() 
    front.menu()