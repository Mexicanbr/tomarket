import json
import random
from urllib.parse import parse_qs, unquote
from colorama import Fore, Style, init
import time
from tomarket import Tomarket, print_timestamp
import sys

def load_credentials():
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        return queries
    except FileNotFoundError:
        print("Arquivo query_id.txt não encontrado.")
        return [  ]
    except Exception as e:
        print("Ocorreu um erro ao carregar o token:", str(e))
        return [  ]

def parse_query(query: str):
    parsed_query = parse_qs(query)
    parsed_query = {k: v[0] for k, v in parsed_query.items()}
    user_data = json.loads(unquote(parsed_query['user']))
    parsed_query['user'] = user_data
    return parsed_query

def get(id):
        tokens = json.loads(open("tokens.json").read())
        if str(id) not in tokens.keys():
            return None
        return tokens[str(id)]

def save(id, token):
        tokens = json.loads(open("tokens.json").read())
        tokens[str(id)] = token
        open("tokens.json", "w").write(json.dumps(tokens, indent=4))

def generate_token():
    tom = Tomarket()
    queries = load_credentials()
    sum = len(queries)
    for index, query in enumerate(queries):
            parse = parse_query(query)
            user = parse.get('user')
            print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ Conta {index+1}/{sum} {user.get('username','')} ]{Style.RESET_ALL}")
            token = get(user['id'])
            if token == None:
                print_timestamp("Gerando token...")
                time.sleep(2)
                token = tom.user_login(query)
                save(user.get('id'), token)
                print_timestamp("Token gerado com sucesso!")

def main():
    init(autoreset=True)
    tom = Tomarket()
    auto_task = input("auto limpar tarefa s/n  : ").strip().lower()
    auto_game = input("auto jogar jogo  s/n  : ").strip().lower()
    auto_combo = input("auto coletar combo quebra-cabeça s/n : ").strip().lower()
    random_number = input("definir pontuação aleatória no jogo 300-500 s/n  : ").strip().lower()
    free_raffle = input("ativar sorteio grátis s/n  : ").strip().lower()
    used_stars = input("usar estrela para: 1. melhorar rank | 2. giro automático | n.(pular tudo) (1/2/n): ").strip().lower()
    
    while True:
        queries = load_credentials()
        sum = len(queries)
        delay = int(3 * random.randint(3700, 3750))
        # generate_token()
        start_time = time.time()
                
        for index, query in enumerate(queries):
            mid_time = time.time()
            total = delay - (mid_time-start_time)
            parse = parse_query(query)
            user = parse.get('user')
            token = get(user['id'])
            if token == None:
                token = tom.user_login(query)
                save(user.get('id'), token)
                time.sleep(2)
            print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ Conta {index+1}/{sum} {user.get('username','')} ]{Style.RESET_ALL}")
            tom.rank_data(token=token, selector=used_stars)
            time.sleep(2)
            tom.claim_daily(token=token)
            time.sleep(2)
            tom.start_farm(token=token)
            time.sleep(2)
            if free_raffle == "s":
                tom.free_spin(token=token, query=query)
            time.sleep(2)
        
        if auto_task == 's':
            for index, query in enumerate(queries):
                mid_time = time.time()
                total = delay - (mid_time-start_time)
                if total <= 0:
                    break
                parse = parse_query(query)
                user = parse.get('user')
                token = get(user['id'])
                if token == None:
                    token = tom.user_login(query)
                print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ Conta {index+1}/{sum} {user.get('username','')} ]{Style.RESET_ALL}")
                tom.list_tasks(token=token,query=query)
                if auto_combo == 's':
                    tom.puzzle_task(token, query)
                time.sleep(2)   
                
        if auto_game == 's':
            for index, query in enumerate(queries):
                mid_time = time.time()
                total = delay - (mid_time-start_time)
                if total <= 0:
                    break
                parse = parse_query(query)
                user = parse.get('user')
                token = get(user['id'])
                if token == None:
                    token = tom.user_login(query)
                print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ Conta {index+1}/{sum} {user.get('username','')} ]{Style.RESET_ALL}")
                tom.user_balance(token=token, random_number=random_number)
                time.sleep(2)

        end_time = time.time()
        total = delay - (end_time-start_time)
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{Fore.YELLOW + Style.BRIGHT}[ Reiniciando em {int(hours)} Horas {int(minutes)} Minutos {int(seconds)} Segundos ]{Style.RESET_ALL}")
        if total > 0:
            time.sleep(total)

from colorama import Fore, Style, init

def start():
    # Inicializar o colorama para permitir o uso das cores
    init(autoreset=True)

    print(Fore.RED + Style.BRIGHT + """
.##.....##.########.##.....##.####..######.....###....##....##.########..########.
.###...###.##........##...##...##..##....##...##.##...###...##.##.....##.##.....##
.####.####.##.........##.##....##..##........##...##..####..##.##.....##.##.....##
.##.###.##.######......###.....##..##.......##.....##.##.##.##.########..########.
.##.....##.##.........##.##....##..##.......#########.##..####.##.....##.##...##..
.##.....##.##........##...##...##..##....##.##.....##.##...###.##.....##.##....##.
.##.....##.########.##.....##.####..######..##.....##.##....##.########..##.....##

          
                  Tomarket Auto Tarefa e Jogo By MexicanBR
                    Canal de script : https://t.me/MexicanbrScripts
                    Canal de airdrop : https://t.me/DiegolaNftCrypto
                        Nota : É NECESSÁRIO PARTICIPAR DO MEU CANAL TELEGRAM
              
        selecione uma opção:
        1. coletar diário
        2. gerar token
          
          """)
    selector = input("Selecione uma opção  : ").strip().lower()

    if selector == '1':
        main()
    elif selector == '2':
        generate_token()
    else:
        exit()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print_timestamp(f"{Fore.RED + Style.BRIGHT}[ {e} ]{Style.RESET_ALL}")
    except KeyboardInterrupt:
        sys.exit(0)
