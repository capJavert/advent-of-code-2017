import requests
import threading


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/Lv1hb8pF")
    request.encoding = 'ISO-8859-1'

    return request.text


def is_numeric(value):
    try:
        int(value)

        return True
    except ValueError:
        return False


class Program (threading.Thread):
    def __init__(self, thread_id, other_id, code):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.other_id = other_id
        self.code = code

    def run(self):
        global snd_counter, lock, frequencies
        try:
            registers = {chr(i): 0 for i in range(97, 113)}
            registers["p"] = self.thread_id

            index = 0

            while index < len(self.code):
                command = self.code[index].split(" ")
                next_index = 1

                if "snd" in command:
                    if not is_numeric(command[1]):
                        frequencies[self.other_id].append(registers[command[1]])
                    else:
                        frequencies[self.other_id].append(command[1])

                    if self.thread_id == 1:
                        snd_counter += 1

                if "set" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] = registers[command[2]]
                    else:
                        registers[command[1]] = int(command[2])

                if "add" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] += registers[command[2]]
                    else:
                        registers[command[1]] += int(command[2])

                if "mul" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] *= registers[command[2]]
                    else:
                        registers[command[1]] *= int(command[2])

                if "mod" in command:
                    if not is_numeric(command[2]):
                        registers[command[1]] %= registers[command[2]]
                    else:
                        registers[command[1]] %= int(command[2])

                if "rcv" in command:
                    lock.acquire()

                    if len(frequencies[self.thread_id]) > 0:
                        registers[command[1]] = frequencies[self.thread_id].pop(0)
                        lock.release()
                    elif len(frequencies[self.thread_id]) == 0 and len(frequencies[self.other_id]) == 0:
                        lock.release()
                        break
                    else:
                        lock.release()
                        continue

                if "jgz" in command:
                    if not is_numeric(command[1]):
                        value = registers[command[1]]
                    else:
                        value = int(command[1])

                    if value > 0:
                        if not is_numeric(command[2]):
                            next_index = registers[command[2]]
                        else:
                            next_index = int(command[2])

                index += next_index

        except Exception as e:
            print(e)

        if self.thread_id == 1:
            lock.acquire()
            print(snd_counter)
            lock.release()


frequencies = [[], []]
snd_counter = 0
lock = threading.Lock()


def main():
    data = get_and_prepare_data_string().splitlines()

    threads = []

    program1 = Program(0, 1, list(data))
    program2 = Program(1, 0, list(data))

    program1.start()
    program2.start()

    threads.append(program1)
    threads.append(program2)

    for t in threads:
        t.join()


main()
