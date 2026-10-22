from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

url = ...

async_engine = create_async_engine()

Session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=True)