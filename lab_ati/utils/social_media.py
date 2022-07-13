def add_social_media(model_obj, formset):
    """
    Add SocialMedia to Empleado, Empresa, ...
    """

    instances = formset.save(commit=False)
    for socialmedia in instances:
        # do something with instance
        socialmedia.content_object = model_obj
        socialmedia.save()
