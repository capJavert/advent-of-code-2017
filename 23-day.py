import requests
import threading


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/HjJwLrW9")
    request.encoding = 'ISO-8859-1'

    return request.text


def is_numeric(value):
    try:
        int(value)

        return True
    except ValueError:
        return False


class Program (threading.Thread):
    def __init__(self, thread_id, code):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.code = code

    def run(self):
        global mul_counter, lock
        try:
            registers = {chr(i): 0 for i in range(97, 105)}

            index = 0

            while index < len(self.code):
                command = self.code[index].split(" ")
                next_index = 1

                if "set" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] = registers[command[2]]
                    else:
                        registers[command[1]] = int(command[2])

                if "sub" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] -= registers[command[2]]
                    else:
                        registers[command[1]] -= int(command[2])

                if "mul" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] *= registers[command[2]]
                    else:
                        registers[command[1]] *= int(command[2])

                    mul_counter += 1

                if "jnz" in command:
                    if not is_numeric(command[1]):
                        value = registers[command[1]]
                    else:
                        value = int(command[1])

                    if value != 0:
                        if not is_numeric(command[2]):
                            next_index = registers[command[2]]
                        else:
                            next_index = int(command[2])

                index += next_index

        except Exception as e:
            print(e)

        lock.acquire()
        print(mul_counter)
        lock.release()


mul_counter = 0
lock = threading.Lock()


def main():
    data = get_and_prepare_data_string().splitlines()

    threads = []

    program1 = Program(0, list(data))

    program1.start()

    threads.append(program1)

    for t in threads:
        t.join()


main()
