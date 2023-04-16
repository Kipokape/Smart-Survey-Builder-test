import { include } from 'named-urls'

export default {
    home: "/",

    profile: "/profile/",

    auth: include('/auth/', {
        login: "login/",
        logout: "logout/"
    }),

    polls: include('/polls/', {
        all: '',
        create: "create/",
        constructor: "constructor/:poll/",

        passing: {
            to: ":slug/",
        }
    }),
}