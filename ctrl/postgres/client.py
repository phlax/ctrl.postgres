import uuid

import asyncpg


class PostgresClient(object):

    async def sql(self, sql):
        conn = await asyncpg.connect(
            user='postgres',
            host='/sockets/postgres')
        values = await conn.fetch(sql)
        await conn.close()
        return values

    async def list_dbs(self):
        return [
            record['datname']
            for record
            in await self.sql(
                '''SELECT datname FROM pg_database '''
                '''WHERE datistemplate = false;''')]

    async def create_db(self, name, encoding='utf8', locale='en_US.utf8',
                        template='template0', user=None):
        if name in await self.list_dbs():
            return ['Database exists']
        username = user or name
        users = [u['usename'] for u in await self.list_users()]
        password = (
            await self.create_user(username)
            if username not in users
            else None)
        await self.sql(
            "CREATE DATABASE %s ENCODING '%s' "
            "LC_COLLATE = '%s' LC_CTYPE = '%s' TEMPLATE = %s"
            % (name, encoding, locale, locale, template))
        if password:
            return [
                'Created db/user/password: %s/%s/%s'
                % (name, username, password)]
        else:
            return ['Created db: %ss' % name]

    async def create_user(self, username):
        print('Adding user %s' % username)
        password = uuid.uuid4().hex[:10]
        await self.sql(
            "CREATE USER %s with PASSWORD '%s'"
            % (username, password))
        return password

    async def drop_db(self, name):
        if name not in await self.list_dbs():
            return ['Database doesnt exist: %s' % name]
        await self.sql("DROP DATABASE %s" % name)
        return ['dropped db: %s' % name]

    async def list_users(self):
        return await self.sql(
            '''SELECT u.usename, u.usesysid
            FROM pg_catalog.pg_user u
            ''')

    async def reset_password(self, name):
        print('resetting password for: %s' % name)
        return 'password reset for: %s' % name

    async def set_owner(self, database, username):
        print(
            'Setting owner %s --> %s'
            % (username, database))
        password = uuid.uuid4().hex[:10]
        await self.sql(
            "ALTER DATABASE %s OWNER TO %s"
            % (database, username))
        return 'Database owner updated'
