from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import ValidationError

class MediaForm(FlaskForm):
    file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp', 'mp4', 'mov'], message='File type not allowed.')])

    def validate_file(self, field):
        # 50 MB Limit
        if field.data and len(field.data.read()) > 50 * 1024 * 1024:
            raise ValidationError('File size exceeds limit of 50MB.')