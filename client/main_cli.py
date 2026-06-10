from cli.front import UserFrontendCLI
import sys
token = sys.argv[1]
sys.stdout.write(f'ТОКЕН: {token}\n')
if __name__ == '__main__':
    while True:
        front = UserFrontendCLI(token) 
        front.menu()
