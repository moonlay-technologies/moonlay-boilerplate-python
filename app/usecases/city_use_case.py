from app import db
from app.models.city_model import City

class CityUseCase:
    pagination = None

    def get_list_city(self, page=1, page_size=10):

        cities = City.query.paginate(page=page, per_page=page_size, error_out=False)
        result = [city.to_dict() for city in cities]

        self.pagination = {
            "page": cities.page,
            "per_page": cities.per_page,
            "pages": cities.pages,
            "total": cities.total,
        }

        if not cities:
            return None
        
        return result

    def get_city_by_id(self, city_id):
        city = City.query.get(city_id)

        if not city:
            return None

        result = city.to_dict()
        
        return result
    
    def create_city(self, name, country):

        city = City(name=name, country=country)
        db.session.add(city)
        db.session.commit()

        if not city:
            return None

        return city.to_dict()  
    
    def update_city(self, city_id, name, country):
        city = City.query.get(city_id)

        if not city:
            return None
        
        city.name = name
        city.country = country

        db.session.commit()
        return city.to_dict()
    
    def delete_city(self, city_id):
        city = City.query.get(city_id)
        if not city:
            return None
        
        db.session.delete(city)
        db.session.commit()
        return {"message": "City deleted successfully"}