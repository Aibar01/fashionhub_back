const ru = {
    header: 'Скоро запускаем! 🚀',
    content: 'Fashionhub.kz - первая в Казахстане сеть для творчества и поиска работы в<br/> Интернете, посвященная исключительно моде, розничной торговле, красоте,<br/> косметике, цифровым технологиям и медиа.',
    mobile_content: 'Первая платформа для поиска работы и стажировок в сфере моды и продаж в Казахстане',
    email_text: 'Получите уведомление, когда мы запустим',
    button_text: 'Отправить',
    congratulation_text: 'Спасибо за ваш интерес. Мы обязательно вас оповестим!',
}

const en = {
    header: 'We are launching soon! 🚀',
    content: 'Fashionhub.kz is the very first online creative and job search network in <br>Kazakhstan, solely dedicated for fashion, retail, beauty, cosmetics, <br>digital and media.',
    mobile_content: 'The first platform for job search and internships in fashion and sales in Kazakhstan.',
    email_text: 'Get notified when we launch',
    button_text: 'Notify me',
    congratulation_text: 'Thank you for your interest. We will definitely notify you!',
}

const changeLang = (language) => {
    console.log(language)
    if (language === 'EN') {
        document.getElementById("soon").innerHTML = en.header;
        document.getElementById("description").innerHTML = en.content;
        document.getElementById("secont").innerHTML = en.mobile_content;
        document.getElementById("notification").innerHTML = en.email_text;
        document.getElementById("submit").innerHTML = en.button_text;
        document.getElementById("cong_text").innerHTML = en.congratulation_text;

        document.getElementById("lang").innerHTML = "EN"
    } else {
        document.getElementById("soon").innerHTML = ru.header;
        document.getElementById("description").innerHTML = ru.content;
        document.getElementById("secont").innerHTML = ru.mobile_content;
        document.getElementById("notification").innerHTML = ru.email_text;
        document.getElementById("submit").innerHTML = ru.button_text;
        document.getElementById("cong_text").innerHTML = ru.congratulation_text;

        document.getElementById("lang").innerHTML = "RU"
    }
}