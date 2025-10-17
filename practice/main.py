import sample_module

def get_sample_module():
    return {"id":"11", "name":"Alok"}
if __name__ == '__main__':
    print("Before",sample_module.get_data())
    sample_module.get_data = get_sample_module
    print("After",sample_module.get_data())
