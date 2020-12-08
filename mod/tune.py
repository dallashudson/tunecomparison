from openpyxl import load_workbook


class TUNE:
    def __init__(self, part_number):
        self.part_number = part_number
        self.rev = None
        self.parts = dict()
        self.type = "tune"
        # self.name = ""
        # self.project_number = self.part_number.split('-')[1]

    def add_subkit(self, part_number, rev, qty):
        self.parts[part_number] = Subkit(part_number, rev, qty)
        return self.parts[part_number]

    def read_tune(self, filename):

        with open(filename) as f:
            next(f)
            index = 2
            data = []
            for line in f:
                data.append(line[(len(str(index))+1):(len(str(index))+7)])
                index += 1
        print(data)
        return data

    def print_tune(self):
        self._print_tune(self)

    def _print_tune(self, tune):
        # print(tune.part_number)

        for part in tune.parts:
            print(tune.parts[part].type, tune.part_number, part,
                  tune.parts[part].qty, tune.parts[part].rev)

            if tune.parts[part].type == 'sub-kit':
                self._print_tune(tune.parts[part])
