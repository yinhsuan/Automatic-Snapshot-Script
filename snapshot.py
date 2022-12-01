
import subprocess as sp
import argparse


def create_snapshot(dataset):
    print("create")

def list_snapshot(dataset):
    snapshots = []
    output = sp.run(['zfs', 'list', '-t', 'snapshot'], stdout=sp.PIPE).stdout
    output = output.decode()
    for i, line in enumerate(output.split('\n')[1:]):
        cols = line.split(' ')
        if cols:
            s = cols[0].split('@')
            if s[1:] and (not dataset or s[0] == dataset):
                snapshots.append({
                    'id': i+1,
                    'dataset': s[0],
                    'create_time': s[1]})
    for ss in snapshots:
        # if Id == None or Id == ss['id']:
        print('%-20d%-20s%-20s' % (ss['id'], ss['dataset'], ss['create_time']))

def delete_snapshot(dataset):
    print("delete")





def backup(create, list, delete, dataset, args):
    if create:
        rotation_cnt = args.rotation_cnt
        create_snapshot(dataset, rotation_cnt)
    elif list:
        list_snapshot(dataset)
    elif delete:
        delete_snapshot(dataset)
    else:
        print("Usage:")
        print("- create: zfsbak DATASET [ROTATION_CNT]")
        print("- list: zfsbak -l|--list [DATASET|ID|DATASET ID]")
        print("- delete: zfsbak -d|--delete [DATASET|ID|DATASET ID...]")
        print("- export: zfsbak -e|--export DATASET [ID]")
        print("- import: zfsbak -i|--import FILENAME DATASET")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', "-c", default=False, dest="create")
    parser.add_argument('--list', "-l", default=False, dest="list")
    parser.add_argument('--delete', "-d", default=False, dest="delete")
    # parser.add_argument('--dataset', type=str)
    # parser.add_argument('--export', type=bool)
    # parser.add_argument('--import_s', type=bool)
    args = parser.parse_args()

    backup(args.create, args.list, args.delete, args)