import keyboard
import time

# def helloWorld(message="Hello World"):
#     print(message)
# helloWorld()
#
# f = open('test_1.txt', 'w')

# f = open('test_1.txt', 'w')  # w overrides all file
#
# f.write('Hi how are you?')
#
# f.close()
#
# f = open('test_1.txt')
#
# print(f.read())
#
# f.close()

# with open('test_1.txt') as f:
#     print(f.read())

# def my_list():
#     with open('shopping_list.txt', 'a') as file:
#         item = input('Enter Item: ')
#         file.write(item + '\n')
#
#
# my_list()
#
#
# # my trial
# def func(bye):
#     print(bye)
#
#
# a = bool
# a = 2


# keyboard.on_press_key('', lambda _: , True)

f = open('shopping_list.txt', 'a+')
d = open('shopping_list.txt', 'r')
shopping_list = []
item_id = 0
list_length_x = 1
list_length_y = 2
canvas = []


def shopping_list_func():
    def add_list():
        for item in shopping_list:
            f.write("•" + item['text'] + "\n\n")

    def is_there(item):
        list_have = False
        for items in shopping_list:
            if items['text'] == item:
                list_have = True
        return list_have

    def delete_list(item_id):
        global list_length_x
        print(item_id)
        for ids in shopping_list:
            if int(ids['id']) == int(item_id):
                index = shopping_list.index(ids)
                shopping_list.pop(index)
                canvas.pop(index)
                list_length_x = list_length_x - 1

    def show_list():
        global list_length_x
        if len(shopping_list) == list_length_x:
            list_length_x = list_length_x + 1

        for a in range(list_length_x):
            arr = []
            for b in range(list_length_y):
                arr.append(" ")
            canvas.append(arr)

        def show_in_canvas():
            for a in shopping_list:
                index = shopping_list.index(a)
                canvas[index][0] = a['text']
                canvas[index][1] = a['id']

        show_in_canvas()

        for c in range(list_length_x):
            print(canvas[c])

    def get_all_list():
        print(f.read())

    def main():
        global item_id
        global take_action
        a = input('Enter item: ')
        if a == "-exit":
            print('canceled action')
            take_action()
        if (is_there(a)):
            print(f'Oops {a} is already in list.')
            a = input('Enter Item: ')
        shopping_list.append({'text': a, 'id': item_id})
        item_id += 1
        show_list()

        def take_action():
            b = input('Enter action: ')
            if b.strip() == '--help':
                print('actions : add, quit, delete, cancel, all')
                print('-exit for cancel action')
                print('For more detailed info : --help {action}')
                take_action()
            if b.strip() == "--help add":
                print('Add item to list')
                take_action()
            if b.strip() == "--help quit":
                print('Accept list and quit app.')
                take_action()
            if b.strip() == "--help delete":
                print('Delete item  from list with id')
                take_action()
            if b.strip() == "help cancel":
                print('Cancel list. Delete all items')
            elif b.strip() == 'add':
                main()
            elif b.strip() == 'all':
                get_all_list()
                take_action()
            elif b == 'quit'.strip():
                print('list finished')
                print('adding items ...')
                add_list()
                f.close()
                return
            elif b.strip() == 'delete':
                global shopping_list
                show_list()
                global c

                c = input('id: ')
                if c == '-exit':
                    print('canceled delete')
                    take_action()
                for items in shopping_list:
                    if int(items['id']) == int(c):
                        index = shopping_list.index(items)
                        print(f'Deleted item : {shopping_list[index]["text"]}')
                delete_list(c)
                show_list()
                take_action()
            elif b == 'cancel'.strip():
                shopping_list = [],
                print('List canceled')
                print('All items Deleted')
                print('Do you want to start again ?')
                c = input('yes/no: ')
                if c == 'yes'.strip() or c == ''.strip():
                    main()
                else:
                    print('all List Canceled.')

            else:
                print(f'there is no command : {b}')
                print('for list of commands type --help')
                take_action()

        take_action()

    main()


read_text = f.read()
d = d.read()
if len(d) > 0:
    d = input("There is already a list. Reset list ? yes/no :")
    if d == 'yes' or d == 'y':
        f = open('shopping_list.txt', 'w+')
        shopping_list_func()
    elif d == 'no' or d == 'n':
        shopping_list_func()
    else:
        print('type yes or no')
else:
    shopping_list_func()
