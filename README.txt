Bookstore API Template (Modular Django Style)

Structure:
- models/           => Separate files for each model (Author, Book)
- serializers/      => Serializers split per model
- views/            => View classes for APIs
- repositories/     => For data access logic (queries, filters)
- services/         => Business logic layer
- utils/            => Common utilities, validation, custom response handlers

Use:
1. Add this 'library' folder into your Django project.
2. Replace sample logic with your actual model, view, serializer code.
3. Include 'library.urls' in your main urls.py using `include()`.
4. Run `python manage.py makemigrations` and `migrate`.

Enjoy clean and scalable Django development!
