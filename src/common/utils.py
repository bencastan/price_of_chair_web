from passlib.hash import pbkdf2_sha512


class Utils(object):

    @staticmethod
    def has_password(password):
        """
        Hashes a password using pbkdf2_512
        :param password: The sha512 password from the login/register form
        :return: A sha512 -> pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password that the user sent matches the database.
        The database password is encrypted more than the user's password at this stage.
        :param password: sha512 - hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if passwords match, false otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)