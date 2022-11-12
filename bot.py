def main():
    run = True
    while run:
        ui = input("Type here: ")
        if ui == "/stop":
            run = False
    return

main()