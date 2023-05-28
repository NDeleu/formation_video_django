from django import forms
from .models import Author, Book


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Auteur")

    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']
        labels = {'title': 'Titre', 'quantity': 'Quantité'}

    # ajouter une methode de validation specifique qui commence tj par clean_
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        if quantity <= 0 or quantity > 100:
            raise forms.ValidationError("La quantité du livre doit être comprise entre 1 et 100")

        return quantity

    # après les clean_ , si on veut un clean global :
    def clean(self):
        title = self.cleaned_data.get('title')
        quantity = self.cleaned_data.get('quantity')

        if title and quantity:
            if title.startswith('Dragon Ball') and quantity < 10:
                raise forms.ValidationError("Minimum une quantité de 10 pour un livre Dragon Ball")

        return self.cleaned_data


"""
username = forms.CharField(label="Nom d'utilisateur", 
                            max_length=25, 
                            help_text="bla bla bla",
                            required = True)
                            
choix à cocher pour booleen :
    publicate = forms.CharField(label="Publier le contenu ?", widget=forms.CheckboxInput)

    CharField
"""

"""
class SomeForms(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=25)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    bio = forms.CharField(label="Biographie", widget=forms.Textarea)

    languages = [('c', 'Langage C'), ('php', 'langage PHP')]
    language = forms.MultipleChoiceField(label="Langages connus", widget=forms.CheckboxSelectMultiple, choices=languages)

    colors = [('1', "Rouge"), ('2', "Bleu"), ('3', "Vert")]
    color = forms.ChoiceField(label="Couleur Dominante", choices=colors, widget=forms.RadioSelect)

    countries = [('fr', "France"), ('jp', "Japon"), ('kr', "Corée du Sud")]
    country = forms.ChoiceField(label="Pays", choices=countries)
"""

