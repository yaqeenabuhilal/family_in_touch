from django.test import TestCase, Client
from django.urls import reverse
from .models import TeengerFeedback
from .forms import CreatTeengerFeedbackForm
from django.test import TestCase
from django.urls import reverse
from .models import User, TeengerFeedback


class TestSummaryForTeengerView(TestCase):
    def setUp(self):
        # Create a test user (teenger)
        self.teenger = User.objects.create(username='test_teenger')
        # Create some teenger feedback
        self.feedback1 = TeengerFeedback.objects.create(Teengers=self.teenger, text="Test Feedback 1",date="2022-03-01",sammary="ff")
        self.feedback2 = TeengerFeedback.objects.create(Teengers=self.teenger, text="Test Feedback 2",date="2022-04-01",sammary="ff")

    def test_summary_for_teenger_view(self):
        # URL for the summary for teenger view
        url = reverse('sammaryforteenger', args=[self.teenger.username])

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        #
        # # Check that the correct template is used
        self.assertTemplateUsed(response, 'ourapp/sammaryforteenger.html')

        # Check that teenger_feedback is passed to the template context
        self.assertIn('teenger_feedback', response.context)
        #
        # # Check that the correct teenger is passed to the template context
        self.assertIn('teenger', response.context)
        self.assertEqual(response.context['teenger'], self.teenger)

        # Check that teenger_feedback contains the correct feedback
        teenger_feedback = response.context['teenger_feedback']
        # self.assertEqual(teenger_feedback1.count(), 2)
        self.assertIn(self.feedback1, teenger_feedback)
        self.assertIn(self.feedback2, teenger_feedback)
