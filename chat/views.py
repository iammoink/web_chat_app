from django.views.generic import TemplateView

# Create your views here.
class ChatBoxView(TemplateView):
    template_name = 'chat/chatbox.html'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['chat_box_name'] = self.kwargs['chat_box_name']
        return context