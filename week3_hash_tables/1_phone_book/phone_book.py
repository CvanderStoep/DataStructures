# python3
import copy
from collections import namedtuple


Contact = namedtuple("Contact", ["name", "number"])


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries_namedtuple(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name (pop & add new named tuple)
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
            contacts.append(Contact(cur_query.name, cur_query.number))
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # using direct addressing scheme
    contacts = [None] * 10**7
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        else:
            if contacts[cur_query.number] is None:
                result.append('not found')
            else:
                result.append(contacts[cur_query.number])
    return result

if __name__ == '__main__':
    # we use a deepcopy of the query, because the naive algorithm overwrites the query !!!
    queries = read_queries()
    queries2 = copy.deepcopy(queries)
    write_responses(process_queries_naive(queries2))
    print('---')
    write_responses(process_queries_namedtuple(queries))
    print('---')
    write_responses(process_queries(queries))
    # write_responses(process_queries_naive(read_queries()))
    # write_responses(process_queries(read_queries()))

