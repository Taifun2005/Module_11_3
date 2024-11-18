import inspect

def introspection_info(obj):
    info = {}
    # attributes_, methods_, module_ =  [], [], []
    type_ = type(obj).__name__
    attributes_ = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods_ = [method for method in dir(obj) if callable(getattr(obj, method))]
    module_ = inspect.getmodule(obj)
    # module_ = obj.__module__ if hasattr(obj, '__module__') else None
    # for i in dir(obj):
    #     if i == inspect.ismodule:
    #         attributes_.append(i)
    #     elif i == inspect.ismethod:
    #         methods_.append(i)
    #     elif i == inspect.ismodule:
    #         module_.append(i)

    info = {
        'type': type_,
        'attributes': attributes_,
        'methods': methods_,
        'module': module_
    }
    return info


number_info = introspection_info('False')
print(number_info)