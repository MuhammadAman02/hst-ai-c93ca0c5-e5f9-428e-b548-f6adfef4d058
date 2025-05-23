from nicegui import ui, app
import os

# Configure app
app.title = "LinkedIn Clone"
app.favicon = "🔗"

# Ensure static files directory exists
os.makedirs('app/static/images', exist_ok=True)
os.makedirs('app/static/css', exist_ok=True)

# Mount static files
app.add_static_files('/static', 'app/static')

# Custom CSS for LinkedIn styling
with ui.head():
    ui.html('''
    <style>
        :root {
            --linkedin-blue: #0a66c2;
            --linkedin-light-blue: #70b5f9;
            --linkedin-black: #000000;
            --linkedin-gray: #86888a;
            --linkedin-light-gray: #f3f2ef;
        }
        
        body {
            font-family: -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', 'Fira Sans', Ubuntu, Oxygen, 'Oxygen Sans', Cantarell, 'Droid Sans', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Lucida Grande', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--linkedin-light-gray);
            color: rgba(0, 0, 0, 0.9);
        }
        
        .linkedin-btn-primary {
            background-color: var(--linkedin-blue);
            color: white;
            border-radius: 24px;
            font-weight: 600;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .linkedin-btn-primary:hover {
            background-color: #004182;
        }
        
        .linkedin-btn-secondary {
            background-color: transparent;
            color: rgba(0, 0, 0, 0.6);
            border-radius: 24px;
            font-weight: 600;
            padding: 12px 24px;
            border: 1px solid rgba(0, 0, 0, 0.6);
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .linkedin-btn-secondary:hover {
            background-color: rgba(0, 0, 0, 0.08);
        }
        
        .navbar {
            background-color: white;
            box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .hero-section {
            background-color: white;
            padding: 40px 0;
        }
        
        .hero-title {
            color: #8f5849;
            font-size: 56px;
            font-weight: 200;
            line-height: 70px;
        }
        
        .feature-card {
            background-color: white;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
            height: 100%;
        }
        
        .feature-card:hover {
            box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.15);
        }
        
        .testimonial-card {
            background-color: white;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
        }
        
        .footer {
            background-color: white;
            padding: 24px 0;
            color: rgba(0, 0, 0, 0.6);
        }
        
        .footer-link {
            color: rgba(0, 0, 0, 0.6);
            text-decoration: none;
            margin-right: 16px;
            font-size: 14px;
        }
        
        .footer-link:hover {
            color: var(--linkedin-blue);
            text-decoration: underline;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 32px;
                line-height: 40px;
            }
            
            .navbar-links {
                display: none;
            }
            
            .mobile-menu {
                display: block;
            }
        }
        
        @media (min-width: 769px) {
            .mobile-menu {
                display: none;
            }
        }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ''')

# LinkedIn logo SVG
LINKEDIN_LOGO = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 84 21" preserveAspectRatio="xMinYMin meet" fill="currentColor" width="84" height="21" style="color: #0a66c2;">
    <g>
        <path d="M12.5 2.75a1.75 1.75 0 101.8 1.75 1.75 1.75 0 00-1.8-1.75zM11 8h3v10h-3zM22.34 7.76A4.06 4.06 0 0019 9.39V8h-3v10h3v-5a2.31 2.31 0 012.16-2.5c1.1 0 1.84.82 1.84 2.5v5h3v-6c0-2.4-1.5-4.24-3.66-4.24zM42.28 9.39V8h-3v10h3v-5a2.31 2.31 0 012.16-2.5c1.1 0 1.84.82 1.84 2.5v5h3v-6c0-2.4-1.5-4.24-3.66-4.24a4.06 4.06 0 00-3.34 1.63zM60.4 8h-3v10h3v-5a2.31 2.31 0 012.16-2.5c1.1 0 1.84.82 1.84 2.5v5h3v-6c0-2.4-1.5-4.24-3.66-4.24a4.06 4.06 0 00-3.34 1.63V8zM54.7 4.75A1.75 1.75 0 1052.9 6.5a1.75 1.75 0 001.8-1.75zM53.2 8h3v10h-3zM30.5 8h-3v10h3zM30.5 4.75A1.75 1.75 0 1028.7 6.5a1.75 1.75 0 001.8-1.75z"></path>
    </g>
</svg>
'''

# Main layout
@ui.page('/')
def linkedin_landing_page():
    # Navigation Bar
    with ui.header().classes('navbar w-full py-3'):
        with ui.row().classes('w-full items-center justify-between px-4 md:px-12'):
            # Logo and search
            with ui.row().classes('items-center gap-2'):
                ui.html(LINKEDIN_LOGO)
                
                with ui.element('div').classes('hidden md:block relative ml-4'):
                    ui.input(placeholder='Search').classes('py-1 pl-8 pr-2 rounded bg-gray-100')
                    ui.icon('search').classes('absolute left-2 top-2 text-gray-500')
            
            # Navigation links - visible on desktop
            with ui.row().classes('navbar-links items-center gap-6'):
                with ui.element('div').classes('flex flex-col items-center'):
                    ui.icon('home').classes('text-2xl text-gray-600')
                    ui.label('Home').classes('text-xs')
                
                with ui.element('div').classes('flex flex-col items-center'):
                    ui.icon('people').classes('text-2xl text-gray-600')
                    ui.label('My Network').classes('text-xs')
                
                with ui.element('div').classes('flex flex-col items-center'):
                    ui.icon('work').classes('text-2xl text-gray-600')
                    ui.label('Jobs').classes('text-xs')
                
                with ui.element('div').classes('flex flex-col items-center'):
                    ui.icon('chat').classes('text-2xl text-gray-600')
                    ui.label('Messaging').classes('text-xs')
                
                with ui.element('div').classes('flex flex-col items-center'):
                    ui.icon('notifications').classes('text-2xl text-gray-600')
                    ui.label('Notifications').classes('text-xs')
                
                ui.separator().classes('h-8 mx-2')
                
                ui.button('Join now').classes('linkedin-btn-secondary')
                ui.button('Sign in').classes('linkedin-btn-primary')
            
            # Mobile menu icon - visible on mobile
            with ui.element('div').classes('mobile-menu'):
                ui.icon('menu').classes('text-2xl')

    # Hero Section
    with ui.element('section').classes('hero-section'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            with ui.row().classes('items-center flex-col md:flex-row'):
                # Left column - Text content
                with ui.column().classes('w-full md:w-1/2 py-8'):
                    ui.label('Welcome to your professional community').classes('hero-title mb-6')
                    
                    # Sign in form
                    with ui.card().classes('w-full max-w-md bg-transparent shadow-none'):
                        ui.input('Email or phone').classes('w-full mb-3 py-3')
                        with ui.input('Password').classes('w-full mb-3 py-3') as password_input:
                            password_input.props('type=password')
                        
                        ui.link('Forgot password?').classes('text-linkedin-blue mb-4 block')
                        
                        ui.button('Sign in').classes('linkedin-btn-primary w-full mb-4')
                        
                        with ui.element('div').classes('flex items-center my-4'):
                            ui.element('hr').classes('flex-grow border-t border-gray-300')
                            ui.label('or').classes('mx-4 text-gray-500')
                            ui.element('hr').classes('flex-grow border-t border-gray-300')
                        
                        ui.button('Continue with Google').classes('linkedin-btn-secondary w-full mb-3').on('click', lambda: ui.notify('Google sign-in clicked'))
                        ui.button('New to LinkedIn? Join now').classes('linkedin-btn-secondary w-full').on('click', lambda: ui.notify('Join now clicked'))
                
                # Right column - Hero image
                with ui.column().classes('w-full md:w-1/2 flex justify-center'):
                    ui.image('https://static.licdn.com/aero-v1/sc/h/dxf91zhqd2z6b0bwg85ktm5s4').classes('max-w-full h-auto')

    # Features Section
    with ui.element('section').classes('py-16 bg-white'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            ui.label('Find the right job or internship for you').classes('text-3xl font-light text-center mb-12')
            
            # Job categories
            with ui.grid(columns=2, rows=3).classes('gap-4 md:grid-cols-4'):
                for category in ['Engineering', 'Business Development', 'Finance', 'Marketing', 'Information Technology', 'Human Resources']:
                    with ui.card().classes('feature-card'):
                        ui.label(category).classes('text-lg font-medium mb-2')
                        ui.label(f'{10000 + category.__hash__() % 90000:,} jobs').classes('text-sm text-gray-500')

    # Explore section
    with ui.element('section').classes('py-16 bg-linkedin-light-gray'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            ui.label('Explore topics you are interested in').classes('text-3xl font-light mb-12')
            
            # Topic buttons
            with ui.element('div').classes('flex flex-wrap gap-3'):
                for topic in ['Remote', 'Work from Home', 'Startups', 'Engineering', 'Business', 'Finance', 'Marketing']:
                    ui.button(topic).classes('linkedin-btn-secondary')

    # Testimonials Section
    with ui.element('section').classes('py-16 bg-white'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            ui.label('Join your colleagues, classmates, and friends on LinkedIn').classes('text-3xl font-light text-center mb-12')
            
            with ui.grid(columns=3).classes('gap-6 md:grid-cols-3'):
                for i, (name, title, content) in enumerate([
                    ('Sarah Johnson', 'Marketing Manager', 'LinkedIn helped me connect with industry professionals and find my dream job.'),
                    ('Michael Chen', 'Software Engineer', 'I\'ve built a strong professional network and learned from experts in my field.'),
                    ('Priya Patel', 'Financial Analyst', 'The job recommendations are spot-on, and I love the learning resources.')
                ]):
                    with ui.card().classes('testimonial-card'):
                        with ui.row().classes('items-center mb-4'):
                            ui.avatar(f'{name[0]}').classes('bg-linkedin-blue text-white')
                            with ui.column().classes('ml-3'):
                                ui.label(name).classes('font-medium')
                                ui.label(title).classes('text-sm text-gray-500')
                        ui.label(content).classes('text-gray-700')

    # CTA Section
    with ui.element('section').classes('py-16 bg-linkedin-light-gray text-center'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            ui.label('Connect with people who can help').classes('text-3xl font-light mb-6')
            ui.button('Find people you know').classes('linkedin-btn-primary mx-auto')

    # Post types section
    with ui.element('section').classes('py-16 bg-white'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            ui.label('Post your job for millions of people to see').classes('text-3xl font-light text-center mb-12')
            ui.button('Post a job').classes('linkedin-btn-primary mx-auto')

    # Footer
    with ui.footer().classes('footer py-8'):
        with ui.container().classes('mx-auto px-4 md:px-12'):
            # Logo and copyright
            with ui.row().classes('mb-6'):
                ui.html(LINKEDIN_LOGO)
                ui.label('© 2023').classes('ml-4 text-sm text-gray-500')
            
            # Footer links
            with ui.grid(columns=4).classes('gap-4 mb-6 md:grid-cols-4'):
                for category, links in [
                    ('General', ['Sign Up', 'Help Center', 'About', 'Press', 'Blog', 'Careers']),
                    ('Browse LinkedIn', ['Learning', 'Jobs', 'Salary', 'Mobile', 'Services']),
                    ('Business Solutions', ['Talent', 'Marketing', 'Sales', 'Learning']),
                    ('Directories', ['Members', 'Jobs', 'Companies', 'Featured', 'Learning', 'Posts'])
                ]:
                    with ui.column():
                        ui.label(category).classes('font-medium mb-3')
                        for link in links:
                            ui.link(link, '#').classes('footer-link block mb-2')
            
            # Legal links
            with ui.row().classes('text-sm flex-wrap'):
                for link in ['User Agreement', 'Privacy Policy', 'Community Guidelines', 'Cookie Policy', 'Copyright Policy', 'Send Feedback']:
                    ui.link(link, '#').classes('footer-link')

# Create a placeholder image for the LinkedIn logo
@ui.page('/static/images/linkedin-logo.svg')
def linkedin_logo():
    ui.html(f'''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 84 21" preserveAspectRatio="xMinYMin meet" fill="currentColor" width="84" height="21" style="color: #0a66c2;">
        <g>
            <path d="M12.5 2.75a1.75 1.75 0 101.8 1.75 1.75 1.75 0 00-1.8-1.75zM11 8h3v10h-3zM22.34 7.76A4.06 4.06 0 0019 9.39V8h-3v10h3v-5a2.31 2.31 0 012.16-2.5c1.1 0 1.84.82 1.84 2.5v5h3v-6c0-2.4-1.5-4.24-3.66-4.24zM42.28 9.39V8h-3v10h3v-5a2.31 2.31 0 012.16-2.5c1.1 0 1.84.82 1.84 2.5v5h3v-6c0-2.4-1.5-4.24-3.66-4.24a4.06 4.06 0 00-3.34 1.63zM60.4 8h-3v10h3v-5a2.31 2.31 0 012.16-2.5c1.1 0 1.84.82 1.84 2.5v5h3v-6c0-2.4-1.5-4.24-3.66-4.24a4.06 4.06 0 00-3.34 1.63V8zM54.7 4.75A1.75 1.75 0 1052.9 6.5a1.75 1.75 0 001.8-1.75zM53.2 8h3v10h-3zM30.5 8h-3v10h3zM30.5 4.75A1.75 1.75 0 1028.7 6.5a1.75 1.75 0 001.8-1.75z"></path>
        </g>
    </svg>
    ''')