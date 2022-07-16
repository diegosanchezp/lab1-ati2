def add_social_media(model_obj, formset):
    """
    Add SocialMedia to Empleado, Empresa, ...
    """

    instances = formset.save(commit=False)
    # Add
    for socialmedia in instances:
        socialmedia.content_object = model_obj
        socialmedia.save()

    # Delete
    for socialmedia in formset.deleted_objects:
        socialmedia.delete()
